---
name: polymarket-debugger
description: >
  Expert root-cause analysis and debugging skill for Python trading bots on Polymarket,
  specialized in up/down binary markets (5-min, 15-min, BTC/ETH/SOL/XRP). Use this skill
  whenever the user mentions bugs, errors, unexpected behavior, trades not executing, orders
  failing, wrong positions, crashes, or any issues in their Polymarket trading bot. This skill
  goes beyond surface symptoms — it traces bugs to their ROOT CAUSE across: authentication
  (L1/L2, EIP-712, signature_type), market timing & epoch logic, order placement & fill
  verification, WebSocket stream management, race conditions in async code, position tracking,
  risk management logic, and environment/configuration errors. Trigger this skill even for
  vague reports like "my bot is broken", "trades aren't going through", "it crashes randomly"
  or "it's not making money like expected" — all of these require structured root-cause
  investigation. Do NOT just patch symptoms; always diagnose the underlying system failure.
---

# Polymarket Root-Cause Debugger

A structured debugging methodology for trading bots operating on Polymarket up/down binary markets.
The goal is always to find and fix the **root cause**, not the symptom.

## 🚨 Proactive Audit Mode

**When the user shares code WITHOUT reporting a specific bug**, or says things like:
- "revisa mi bot", "audita mi código", "no sé qué está mal", "muchos bugs que no detecto"
- or shares a file/paste without a clear error message

→ **Do NOT wait for them to describe symptoms. Run a full audit.**

### Pre-Audit: Collect Both Context Layers First

Before auditing, confirm you have:
- **Big Picture**: overall architecture — how many files/modules, what's the main loop, what external APIs does it call?
- **Tactical**: any recent errors, what the bot *should* do vs what it *actually* does

If the user only pastes one file and the bot has multiple modules, ask for the rest. An audit of one file in isolation will miss inter-module bugs.

### Audit Protocol (run in this order):

1. **Auth audit** — Find: missing `set_api_creds()`, wrong `signature_type`, `funder` misconfiguration
2. **Timing audit** — Find: hardcoded token IDs, no epoch recalculation, missing window guards
3. **Order audit** — Find: no fill verification, GTC orders without cleanup, direction logic errors, missing min size/tick checks
4. **Async audit** — Find: shared mutable state without locks, `asyncio.run()` inside async, no rate limit handling
5. **WebSocket audit** — Find: no reconnection logic, no re-subscription, no staleness detection
6. **Position audit** — Find: in-memory-only state (no persistence), no redemption logic, stale balance
7. **Config audit** — Find: env vars accessed before `load_dotenv()`, hardcoded keys, no PID lock
8. **Strategy audit** — Find: fixed price in backtests, look-ahead bias, no confidence threshold, unbounded Kelly

### 🥊 Devil's Advocate Pass (always run last)

After completing the 8-category audit, do one final pass with the explicit question:

> *"¿Qué estoy asumiendo que funciona correctamente y que en realidad podría ser el bug principal?"*

Look specifically at:
- The module that looks the simplest (bugs hide in "obvious" code)
- Any interaction *between* two modules (integration points fail more than individual modules)
- Any code that was recently changed ("it worked before I changed X" = X is the suspect)

### Audit Output Format:

```
## 🔍 AUDITORÍA COMPLETA DEL BOT

### ✅ Correcto
- [things that are properly implemented]

### 🐛 Bugs Encontrados (ordenados por severidad)

#### 🔴 CRÍTICO — [Bug name]
- Archivo/línea: [location]
- Root cause: [the WHY, not the WHAT]
- Causal chain: symptom → immediate cause → root cause
- Fix: [code with ❌/✅/🛡️ pattern]

#### 🟡 MODERADO — [Bug name]  
...

#### 🔵 LATENTE — [Bug name] 
- Condición que lo dispara: [specific trigger condition]
...

### 🥊 Devil's Advocate Finding
[What I almost missed / the assumption I challenged]

### 📋 Checklist de Salud
[full checklist with ✅/❌ per item]
```

**Latent bugs are especially important** — these are bugs that don't crash the bot today but will fail under:
- Market transitions (epoch boundary)
- Network hiccups
- Running for >4 hours
- High volatility (more trades/second)
- After a restart

---

## Guiding Philosophy

> "Every bug has a root cause. A symptom is just the bug's shadow."

**The #1 enemy is the quick fix.** When a user reports a problem, resist the urge to patch. A patch applied without understanding the root cause creates a second bug that's harder to find. Instead, always follow this sequence:

1. Collect **full context** before diagnosing (see Context Engineering below)
2. Classify the failure category
3. Trace the causal chain backward: symptom → root cause → systemic vulnerability
4. Prescribe a fix that eliminates the cause, not just the symptom
5. Add a guard (test/assertion/log) to prevent regression
6. Before writing a single line of fix code, mentally verify it won't break adjacent modules (TDD mindset)

### Context Engineering — How to Request Information

Never diagnose from a symptom alone. Always collect two layers of context:

**Layer 1 — Big Picture Context** (architecture): Ask for / look at the full bot structure. Which modules exist? How do they connect? What's the data flow from "signal detected" → "order placed" → "fill verified"?

**Layer 2 — Tactical Context** (the specific failure): The exact error text + full traceback, the precise input that triggered it, the exact output/behavior observed, and what the user *expected* to happen instead.

If the user only provides one layer, ask for the other before diagnosing. "Garbage in, garbage out" applies directly here — a diagnosis made without Big Picture Context will produce a patch, not a fix.

---

## Step 1: Triage — Classify the Failure

Ask the user for (or extract from their code/logs):
- The **error message** (exact text, stack trace)
- The **behavior observed** vs **behavior expected**
- **When** it happens (always / intermittently / at specific market transitions)
- **What changed** before the bug appeared (new code, new API version, new market type)

Then classify into one of these **root cause categories**:

### Category A: Authentication & Credentials
→ See `references/auth-bugs.md`

Symptoms: `401 Unauthorized`, `Invalid api key`, `403 Forbidden`, orders silently rejected, credentials work in browser but not in code.

### Category B: Market Timing & Epoch Logic
→ See `references/timing-bugs.md`

Symptoms: Bot can't find the active market, trades wrong epoch, misses the window, slug not found, `market closed` errors, stale token IDs.

### Category C: Order Placement & Fill Verification
→ See `references/order-bugs.md`

Symptoms: Order returns success but isn't in order book, partial fills ignored, FOK orders that silently fail, minimum size violations, wrong tick size, buy/sell side confusion.

### Category D: WebSocket & Real-Time Data
→ See `references/websocket-bugs.md`

Symptoms: Bot hangs waiting for price data, stale orderbook used for decisions, missed market open/close events, silent disconnections, reconnection loops.

### Category E: Async Race Conditions
→ See `references/async-bugs.md`

Symptoms: Works in testing, fails under load; orders placed twice; state corrupted between coroutines; `asyncio` event loop errors; `RuntimeError: Event loop is closed`.

### Category F: Position & Portfolio State
→ See `references/position-bugs.md`

Symptoms: Bot thinks it has no position when it does (or vice versa), double-buys same market, doesn't redeem winnings, incorrect P&L tracking.

### Category G: Configuration & Environment
→ See `references/config-bugs.md`

Symptoms: Works on developer machine, fails in production; wrong chain ID; `.env` not loaded; `signature_type` mismatch; funder address vs wallet address confusion.

### Category H: Strategy Logic Errors
→ See `references/strategy-bugs.md`

Symptoms: Bot trades the wrong direction consistently, signal weights wrong, entry at wrong time in window (too early / too late), no stop-loss, Kelly sizing issues.

### Category I: Production vs Development Failures
→ See `references/production-bugs.md`

Symptoms: **Works on my machine** but fails in production; everything shows green checkmarks but no trades are placed; bot works for 2 hours then degrades; schema mismatch between modules; state drift between local DB and Polymarket API.

**This is the hardest category** — all individual components report success but the integrated system fails silently.

---

## Step 2: Root Cause Analysis Protocol

Once classified, follow this chain:

```
SYMPTOM → IMMEDIATE CAUSE → ROOT CAUSE → SYSTEMIC VULNERABILITY
```

**Example:**
- SYMPTOM: `PolyApiException[401]` on `post_order()`
- IMMEDIATE CAUSE: Invalid API credentials passed
- ROOT CAUSE: `create_or_derive_api_creds()` called once at startup, but API keys expire → credentials stale
- SYSTEMIC VULNERABILITY: No credential refresh mechanism, no retry-with-reauth logic

**Always ask these three questions before diagnosing:**
- Is this deterministic or intermittent? → Intermittent = timing, async, or network
- Did it ever work? If yes, what changed?
- Is the bug in the bot's logic or in the API's response?

### 🧠 When Stuck — The Blind Spot Prompt

If analysis isn't converging on a root cause after examining the obvious categories, explicitly ask yourself (and/or the user):

> *"¿Qué no estoy teniendo en cuenta? ¿Es este el mejor camino a seguir? ¿Qué haría alguien que es experto en bots de Polymarket en este escenario?"*

This forces a shift from "assistant mode" (accepting the framing) to "expert mode" (questioning the framing). The bug is often not where it appears to be.

### 🥊 Devil's Advocate Mode

For complex or architecture-level bugs, mentally split into two roles:

- **Architect**: "Given the code structure, what's the most likely root cause?"
- **Devil's Advocate**: "What assumption am I making that could be completely wrong? What if the bug is actually in [the module I haven't looked at yet]?"

Run both hypotheses in parallel. The devil's advocate position finds bugs that single-track analysis misses — especially latent bugs hiding in modules that "look fine."

### 🧪 TDD Verification Before Prescribing a Fix

Before writing any fix code, first write what a passing test would look like:

```python
# What does "fixed" look like?
# Example: If fixing auth retry logic:
# GIVEN: credentials expired mid-session
# WHEN: post_order() receives 401
# THEN: bot re-derives credentials and retries → order succeeds

# Only THEN write the fix that makes this test pass
```

This prevents fixes that solve the reported symptom but break adjacent behavior.

---

## Step 3: Fix Prescription Template

When prescribing a fix, always provide:

```python
# ❌ BROKEN (explains why this is wrong)
# ... problematic code ...

# ✅ FIX (explains the root cause being addressed)
# ... corrected code ...

# 🛡️ GUARD (regression prevention)
# ... assertion / test / log to prevent recurrence ...
```

---

## Step 4: Polymarket-Specific Knowledge Base

### Up/Down Market Structure
- Markets resolve at fixed epoch boundaries: `window_ts = now - (now % 300)` for 5-min markets
- Token IDs change **every epoch** — never hardcode them
- Market slug format: `btc-updown-5m-{window_ts}` (deterministic, no need to search)
- Resolution: last price at window close vs opening price
- Minimum order: **5 shares**; at $0.95/share → $4.75 minimum
- Tick size: `0.01` for most up/down markets — orders must be multiples

### API Architecture (2026)
- **Gamma API**: Market metadata, discovery, resolution info → `https://gamma-api.polymarket.com`
- **CLOB API**: Order placement, order book, fills → `https://clob.polymarket.com`
- **WebSocket**: `wss://ws-subscriptions-clob.polymarket.com/ws/market` and `/ws/user`
- Auth: L1 (EIP-712, wallet signature) → generates L2 (HMAC-SHA256 API key/secret/passphrase)
- `signature_type=0` → EOA/MetaMask; `signature_type=1` → email/Magic/proxy wallet
- `funder` address ≠ signing key address when using proxy wallets

### Known Bugs in py-clob-client (as of early 2026)
- **Pagination bug #182**: `get_orders()` breaks at 500+ orders — use `OpenOrderParams(market=conditionId)`
- **401 on post_order but not cancel**: Often signature_type mismatch; cancel uses different auth path
- **Stale API key**: Keys derived from `create_or_derive_api_creds()` can expire; implement re-derivation

---

## Step 5: Structured Debug Checklist

Present this to the user when they share code or describe their bug:

```
POLYMARKET BOT DEBUG CHECKLIST
================================
AUTH
[ ] signature_type matches wallet type (0=EOA, 1=Magic/email)  
[ ] funder= is proxy wallet address (not signing key address)
[ ] API creds refreshed (not stale from startup)
[ ] chain_id = 137 (Polygon mainnet)

MARKET TIMING
[ ] Token ID fetched fresh each epoch (not cached/hardcoded)
[ ] Epoch boundary calculated correctly: now - (now % 300)
[ ] Market discovery uses Gamma API with correct filter
[ ] Bot enters window with enough time before close

ORDERS
[ ] Size >= 5 shares minimum
[ ] Price is multiple of tick_size (0.01)
[ ] Order side (BUY UP token vs BUY DOWN token) correctly mapped to prediction
[ ] FOK vs GTC chosen correctly (FOK for end-of-window snipe)
[ ] Order fill verified after submission (not just "success" response)
[ ] Positions checked before placing (avoid double-buy)

ASYNC / RUNTIME
[ ] Single event loop (no nested asyncio.run())
[ ] WebSocket reconnection logic present
[ ] Binance/price feed rate limits handled with backoff
[ ] No shared mutable state between coroutines without locks

RISK
[ ] Max position size enforced
[ ] Stop-loss or exit logic present
[ ] Capital allocation doesn't exceed account balance
```

---

## Step 6: Self-Diagnostic Script

The skill includes `scripts/health_check.py` — a ready-to-run Python script that performs static analysis of the user's bot code.

```bash
python scripts/health_check.py --bot-file your_bot.py
```

**When to suggest this script:**
- User says "no sé qué está mal" or "muchos bugs que no detecto"
- User is about to go live for the first time
- After a crash with no clear error
- Ongoing monitoring (add to CI or cron)

The script exits with code 0 (clean) or 1 (critical bugs found) — CI-friendly.

---

## Step 7: When to Read Reference Files

Load the appropriate reference file based on the bug category:

| Category | File | When to Load |
|----------|------|--------------|
| Auth errors | `references/auth-bugs.md` | Any 401/403, credential issues |
| Timing/epoch | `references/timing-bugs.md` | Market not found, wrong epoch |
| Orders | `references/order-bugs.md` | Orders failing, wrong fills |
| WebSocket | `references/websocket-bugs.md` | Stale data, disconnections |
| Async | `references/async-bugs.md` | Race conditions, event loop errors |
| Position state | `references/position-bugs.md` | Double trades, wrong portfolio state |
| Config/env | `references/config-bugs.md` | Works locally not in prod |
| Strategy | `references/strategy-bugs.md` | Wrong direction, bad signals |
| **Production failures** | `references/production-bugs.md` | **Works locally but fails in prod; "green checkmarks" but no trades; bot degrades over time** |
| **Dev workflow** | `references/dev-workflow.md` | **User is building/rebuilding the bot from scratch; architecture decisions; before going live** |
| **Hidden rules** | `references/hidden-rules.md` | **Bug persists after obvious checks; user is new to the system; non-obvious patterns** |

### When to proactively suggest `hidden-rules.md`:
- User has been debugging the same issue for multiple sessions
- Bug is intermittent with no clear pattern
- User says "everything looks correct but..."
- User is about to go live for the first time

### When to proactively suggest `dev-workflow.md`:
- User is starting a new bot or major refactor
- User asks "where do I start?" or "how should I structure this?"
- User mentions they've rewritten the bot before due to it becoming unmaintainable

---

## Output Format

When debugging a reported bug, structure your response as:

```
## 📋 Contexto Recibido
Big Picture: [architecture understood ✅ or missing ⚠️]
Tactical: [error message + traceback ✅ or missing ⚠️]
→ If either layer is missing, request it before proceeding.

## 🔍 Bug Classification
[Category letter + name]

## 🌿 Root Cause (not symptom)
[The actual underlying cause — the WHY]

## 🔗 Causal Chain
Symptom → Immediate Cause → Root Cause → Systemic Vulnerability

## 🥊 Devil's Advocate Check
[What assumption did I challenge? What adjacent module did I verify isn't also affected?]

## 🧪 What "Fixed" Looks Like (TDD)
[GIVEN / WHEN / THEN — what behavior the fix must produce]

## ✅ Fix
[Code with ❌ broken / ✅ fix / 🛡️ guard pattern]

## 🔁 Regression Prevention
[What test/assertion/log prevents this from recurring silently]
```

Always end with: *"¿Quieres que audite otra parte del bot con esta misma metodología?"*
