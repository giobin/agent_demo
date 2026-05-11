"""
MCP Server di Demo — usato dal notebook mcp_demo.ipynb

Espone 4 tool via Model Context Protocol (trasporto stdio).
Avviato automaticamente dal client come subprocess; non serve
aprire un secondo terminale.
"""

from mcp.server.fastmcp import FastMCP
import random
import datetime
import pytz

# FastMCP gestisce l'intero protocollo MCP: registrazione tool,
# serializzazione JSON-RPC e trasporto stdio.
mcp = FastMCP("DemoServer")


# ── Tool 1 ──────────────────────────────────────────────────────────────────
@mcp.tool()
def count_words(text: str) -> int:
    """Conta il numero di parole in un testo.

    Args:
        text: Il testo da analizzare.
    """
    return len(text.split())


# ── Tool 2 ──────────────────────────────────────────────────────────────────
@mcp.tool()
def convert_temperature(value: float, from_unit: str, to_unit: str) -> str:
    """Converte una temperatura tra Celsius (C), Fahrenheit (F) e Kelvin (K).

    Args:
        value: Il valore numerico della temperatura.
        from_unit: Unità di partenza: 'C', 'F' o 'K'.
        to_unit: Unità di arrivo: 'C', 'F' o 'K'.
    """
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # Converte tutto a Celsius come punto intermedio
    to_celsius = {"C": lambda v: v, "F": lambda v: (v - 32) * 5 / 9, "K": lambda v: v - 273.15}
    from_celsius = {"C": lambda v: v, "F": lambda v: v * 9 / 5 + 32, "K": lambda v: v + 273.15}

    if from_unit not in to_celsius or to_unit not in from_celsius:
        return f"Unità non valida. Usa C, F o K."

    celsius = to_celsius[from_unit](value)
    result = from_celsius[to_unit](celsius)
    return f"{value}°{from_unit} = {result:.2f}°{to_unit}"


# ── Tool 3 ──────────────────────────────────────────────────────────────────
@mcp.tool()
def get_current_time(timezone: str) -> str:
    """Restituisce l'ora corrente in un fuso orario specificato.

    Args:
        timezone: Fuso orario IANA valido, es. 'Europe/Rome', 'America/New_York'.
    """
    try:
        tz = pytz.timezone(timezone)
        now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"Ora in {timezone}: {now}"
    except Exception as e:
        return f"Fuso orario non valido '{timezone}': {e}"


# ── Tool 4 ──────────────────────────────────────────────────────────────────
FACTS = [
    "Gli ottopodi hanno tre cuori e sangue blu.",
    "Un giorno su Venere dura più di un anno su Venere.",
    "Il miele non scade: è stato trovato miele commestibile nelle piramidi egizie.",
    "I fenicotteri sono rosa perché mangiano gamberi ricchi di carotenoidi.",
    "Il cervello umano consuma circa il 20% dell'energia totale del corpo.",
    "Le api possono riconoscere i volti umani.",
    "Il suono viaggia 4 volte più velocemente nell'acqua che nell'aria.",
]


@mcp.tool()
def get_random_fact() -> str:
    """Restituisce un fatto curioso casuale dalla collezione del server."""
    return random.choice(FACTS)


# ── Entrypoint ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # mcp.run() avvia il server in modalità stdio:
    # legge richieste JSON-RPC da stdin, scrive risposte su stdout.
    mcp.run()
