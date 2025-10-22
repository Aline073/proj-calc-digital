import qdarktheme
from PySide6.QtWidgets import QApplication
from variables import DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

def setupTheme(app=None, theme_mode='auto'):
    """
    Aplica o tema do qdarktheme e sobrepõe com QSS customizado.
    Se app não for passado, usa a instância ativa de QApplication.
    theme_mode pode ser 'auto', 'dark' ou 'light'.
    """
    if app is None:
        app = QApplication.instance()

    # Aplica o tema base (qdarktheme configura o app internamente)
    qdarktheme.setup_theme(theme_mode)

    # Sobrepõe com QSS customizado
    base_styles = app.styleSheet() or ""
    app.setStyleSheet(base_styles + qss)