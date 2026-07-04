# PrePlanRun

Calculadora de plano de corrida que distribui distância e velocidade ao longo de ciclos de treino, usando progressão geométrica.

Fork do projeto [TiagoTi/preplanrun](https://github.com/TiagoTi/preplanrun).

## O que faz

Dado uma distância total, velocidade inicial, número de ciclos e uma razão de progressão, o script calcula:

- A distância de cada etapa do treino
- A velocidade sugerida para cada ciclo
- O tempo estimado por etapa e o tempo total

## Tecnologias

- Python 3

## Como usar

```bash
git clone https://github.com/Agsterr/preplanrun.git
cd preplanrun
python main.py
```

Edite os parâmetros no final do arquivo `main.py` (`D_total`, `V_inicial`, `C`, `razao`) conforme seu plano de treino.

## Exemplo de saída

O script imprime cada etapa com distância, velocidade e tempo acumulado até completar o total planejado.

## Autor original

[TiagoTi](https://github.com/TiagoTi) — fork mantido por **Agster Junior da Costa Santos**
