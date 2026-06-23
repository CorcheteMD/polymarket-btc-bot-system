---
name: forecast-calibration-engine
description: Evalua calibracion de predicciones, forecasts, probabilidades y estrategias. Usar para Brier score, OOS, walk-forward, PBO, reliability curves, bias y comparacion contra precio de mercado. No genera senales nuevas ni ejecuta trading.
---

# Forecast Calibration Engine

## Mision

Medir si las probabilidades del sistema son confiables antes de convertirlas en riesgo o ejecucion.

## Inputs

- Forecast log o senales historicas.
- Outcomes resueltos.
- Backtests OOS / WFO.
- Reportes: `backtest_plots/calibration.png`, `vault/research/*`, `fair_value_paper_trades_5m.csv`.

## Workflow

1. Distinguir accuracy, calibration y profitability.
2. Calcular Brier score cuando haya probabilidades.
3. Separar IS, OOS, paper y live.
4. Detectar overfitting y PBO cuando hubo busqueda parametrica.
5. Entregar veredicto de confianza.

## Output

- Calibration report.
- Riesgo de overfit.
- Minimo N requerido.
- Handoff a `signal-generation-anomaly` o `risk-management-gate`.

## Fuera De Scope

- No crea una nueva estrategia.
- No aprueba capital real.
- No cambia thresholds por si sola.

