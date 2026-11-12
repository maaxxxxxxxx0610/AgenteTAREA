from mesa.visualization import SolaraViz, make_space_component
from agente import Carro, Semaforo
from modelo import ModeloInterseccion

def agent_portrayal(agent):
    if isinstance(agent, Semaforo):
        return {
            "color": agent.estado,
            "marker": "s",
            "size": 180,
            "zorder": 3
        }
    elif isinstance(agent, Carro):
        color_carro = "dodgerblue" if agent.direccionCarro == "H" else "darkorange"
        return {
            "color": color_carro,
            "marker": "o",
            "size": 120,
            "zorder": 2
        }

def post_process_ax(ax):
    ax.set_facecolor("#2e8b57")
    ax.axhspan(6.5, 7.5, color="#555555", zorder=0)
    ax.axvspan(6.5, 7.5, color="#555555", zorder=0)
    ax.axhline(7, color="white", linestyle="--", linewidth=1, zorder=1)
    ax.axvline(7, color="white", linestyle="--", linewidth=1, zorder=1)
    ax.set_xlim(-0.5, 14.5)
    ax.set_ylim(-0.5, 14.5)
    ax.set_xticks([])
    ax.set_yticks([])

SpaceGraph = make_space_component(agent_portrayal, post_process=post_process_ax)

model_params = {
    "width": 15,
    "height": 15,
    "num_carros": 5
}

modelo_inicial = ModeloInterseccion(width=15, height=15, num_carros=5)

page = SolaraViz(
    modelo_inicial,
    components=[SpaceGraph],
    model_params=model_params,
    name="Interseccion Tarea"
)