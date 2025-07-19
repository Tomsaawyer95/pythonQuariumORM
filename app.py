import sys

from PySide6.QtWidgets import (QApplication, QHeaderView, QTableWidgetItem,
                               QAbstractItemView, QButtonGroup)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

from aquarium_package.models import Type, Sexe ,FishORM,AlgueORM,FishParentORM
from aquarium_package.ecosystem import Aquarium
from aquarium_package.main import do_step
from aquarium_package.factories import create_fish_type
from aquarium_package.services import load_aquarium

class AquariumController:
    def __init__(self, window_app):
        self.window_app = window_app
        self.current_aquarium = Aquarium(-1)
        self.window_app.btn_add_fish.setEnabled(False)
        self.window_app.btn_add_algue.setEnabled(False)
        self.window_app.btn_step.setEnabled(False)
        self.window_app.btn_save_aquarium.setEnabled(False)
        self.window_app.tb_fishs.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.window_app.tb_algues.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        #Gestion bouton radio pour le choix du mode
        self.radio_fish_button_group = QButtonGroup(self.window_app)
        self.radio_fish_button_group.addButton(self.window_app.rb_alea,0)
        self.radio_fish_button_group.addButton(self.window_app.rb_perso,1)
        self.window_app.rb_alea.setChecked(True)
        self.lock_form(True)

        self.setup_ui()

    def setup_ui(self):
        self.window_app.btn_load.clicked.connect(self.initialize_aquarium)
        self.window_app.btn_add_fish.clicked.connect(self.add_fish_to_aquarium)
        self.window_app.btn_add_algue.clicked.connect(self.add_algue_to_aquarium)
        self.window_app.btn_step.clicked.connect(self.do_several_step)
        self.window_app.btn_save_aquarium.clicked.connect(self.save_aquarium)

        self.active_radio_id = self.radio_fish_button_group.checkedId()
        self.radio_fish_button_group.idClicked.connect(self.on_radio_fish_id_changed)

    def on_radio_fish_id_changed(self,id):
        if id == 0 and id != self.active_radio_id:
            self.reset_form()
            self.lock_form(True)
            self.active_radio_id = id
        elif id == 1 and id != self.active_radio_id:
            self.lock_form(False)
            self.active_radio_id = id
        else :
            # Ce bouton est déjà sélectionné → on ignore
            return

    def reset_form(self):
        self.window_app.le_fish_name.clear()
        self.window_app.le_fish_age.clear()
        self.window_app.le_fish_pv.clear()
        self.window_app.cbb_fish_type.setCurrentIndex(0)  # ou setCurrentText("UNKNOWN")
        self.window_app.cbb_fish_sexe.setCurrentIndex(0)

    def lock_form(self,value : bool):
        # Désactiver les QLineEdit
        self.window_app.le_fish_name.setEnabled(not value)
        self.window_app.le_fish_age.setEnabled(not value)
        self.window_app.le_fish_pv.setEnabled(not value)

        # Désactiver les QComboBox
        self.window_app.cbb_fish_type.setEnabled(not value)
        self.window_app.cbb_fish_sexe.setEnabled(not value)

    def initialize_aquarium(self):
        try :
            if  int(self.window_app.le_load.text()):
                aquarium_id = int(self.window_app.le_load.text())
            else:
                aquarium_id = 1
        except :
            aquarium_id = 1
        self.current_aquarium = load_aquarium(aquarium_id)
        self.refresh_table()
        self.window_app.btn_add_fish.setEnabled(True)
        self.window_app.btn_add_algue.setEnabled(True)
        self.window_app.btn_step.setEnabled(True)
        self.window_app.btn_load.setEnabled(False)
        self.window_app.btn_save_aquarium.setEnabled(True)

    def refresh_table(self):
        self.window_app.tb_fishs.clearContents()
        self.window_app.tb_algues.clearContents()

        list_column_fishs = ['id', 'name', 'age', 'pv', 'sexe', 'typeFish', 'aquarium_id']
        self.window_app.tb_fishs.setColumnCount(len(list_column_fishs))
        self.window_app.tb_fishs.setHorizontalHeaderLabels(list_column_fishs)
        self.window_app.tb_fishs.setRowCount(len(self.current_aquarium.get_alive_fishs()))
        self.window_app.tb_fishs.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for i, fish in enumerate(self.current_aquarium.get_alive_fishs()):
            self.window_app.tb_fishs.setItem(i, 0, QTableWidgetItem(str(fish.id)))
            self.window_app.tb_fishs.setItem(i, 1, QTableWidgetItem(fish.name))
            self.window_app.tb_fishs.setItem(i, 2, QTableWidgetItem(str(fish.age)))
            self.window_app.tb_fishs.setItem(i, 3, QTableWidgetItem(str(fish.pv)))
            self.window_app.tb_fishs.setItem(i, 4, QTableWidgetItem(fish.sexe))
            self.window_app.tb_fishs.setItem(i, 5, QTableWidgetItem(fish.type_fish))
            self.window_app.tb_fishs.setItem(i, 6, QTableWidgetItem(str(fish.fish_aquarium_id)))

        list_column_algues = ['id', 'name', 'age', 'pv', 'aquarium_id']
        self.window_app.tb_algues.setColumnCount(len(list_column_algues))
        self.window_app.tb_algues.setHorizontalHeaderLabels(list_column_algues)
        self.window_app.tb_algues.setRowCount(len(self.current_aquarium.get_alive_algues()))
        self.window_app.tb_algues.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for i, algue in enumerate(self.current_aquarium.get_alive_algues()):
            self.window_app.tb_algues.setItem(i, 0, QTableWidgetItem(str(algue.id)))
            self.window_app.tb_algues.setItem(i, 1, QTableWidgetItem(algue.name))
            self.window_app.tb_algues.setItem(i, 2, QTableWidgetItem(str(algue.age)))
            self.window_app.tb_algues.setItem(i, 3, QTableWidgetItem(str(algue.pv)))
            self.window_app.tb_algues.setItem(i, 4, QTableWidgetItem(str(algue.algue_aquarium_id)))

        self.window_app.repaint()

    def add_fish_to_aquarium(self):
        type_fish = Type[self.window_app.cbb_fish_type.currentText()] if \
            self.window_app.cbb_fish_type.currentText() and self.active_radio_id == 1 else None
        sexe = Sexe[self.window_app.cbb_fish_sexe.currentText()] if self.window_app.cbb_fish_sexe.currentText() else None
        age = int(self.window_app.le_fish_age.text()) if self.window_app.le_fish_age.text() else 0
        pv = int(self.window_app.le_fish_pv.text()) if self.window_app.le_fish_pv.text() else 10
        name = self.window_app.le_fish_name.text() if self.window_app.le_fish_name.text() else None
        aquarium_id = self.current_aquarium.id

        fish = create_fish_type(type_fish,sexe,age,pv,name,aquarium_id)
        self.current_aquarium.add_fish(fish)

        self.refresh_table()


    def add_algue_to_aquarium(self):
        age = int(self.window_app.le_algue_age.text()) if self.window_app.le_algue_age.text() else 0
        pv = int(self.window_app.le_algue_pv.text()) if self.window_app.le_algue_pv.text() else 10

        self.current_aquarium.add_algue(age,pv)
        self.refresh_table()

    def do_several_step(self):
        nb_step = int(self.window_app.cbb_nb_iter.currentText())
        for i in range(nb_step):
            print(""" 
            ----------------------- NOUVEAU STEP -----------------------
            ------------------------------------------------------------       
            """)
            do_step(self.current_aquarium)
        self.refresh_table()

    def save_aquarium(self):
        self.current_aquarium.save_to_db()
        self.window_app.btn_add_fish.setEnabled(False)
        self.window_app.btn_add_algue.setEnabled(False)
        self.window_app.btn_step.setEnabled(False)
        self.window_app.btn_load.setEnabled(True)
        self.window_app.btn_save_aquarium.setEnabled(False)
        self.current_aquarium = Aquarium(-1)
        self.refresh_table()

if __name__ == "__main__":
    with open("style.qss", "r") as f:
        style = f.read()

    application = QApplication()
    application.setStyleSheet(style)

    loader = QUiLoader()
    fichier_ui = QFile("./pythonQuariumUI.ui")
    fichier_ui.open(QIODevice.OpenModeFlag.ReadOnly)
    window_app = loader.load(fichier_ui)
    fichier_ui.close()

    window_app.cbb_fish_type.addItems([t.name for t in Type])
    window_app.cbb_fish_type.setCurrentText("UNKNOWN")
    window_app.cbb_fish_sexe.addItem("")
    window_app.cbb_fish_sexe.addItems([s.name for s in Sexe])
    window_app.cbb_nb_iter.addItems([str(i+1) for i in range(20)])

    controller = AquariumController(window_app)

    window_app.show()
    sys.exit(application.exec())
