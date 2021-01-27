from tkinter import Tk, Frame, Label, Button, PhotoImage
from json import loads

root = Tk()
boutons = Frame(root)
legende = Frame(root)
info = Frame(root)

images = {
    'legend': PhotoImage(file="legendes/legende.png"),
    'name': PhotoImage(file="legendes/element.png"),
    'amb_state': PhotoImage(file="legendes/etat.png"),
    'fusion_point': PhotoImage(file="legendes/fusion.png"),
    'boiling_point': PhotoImage(file="legendes/ebullition.png")
}
bar = {
    'name': Label(info, image=images['name']).grid(row=1, column=1),
    'amb_state': Label(info, image=images['amb_state']).grid(row=1, column=2),
    'fusion_point': Label(info, image=images['fusion_point']).grid(row=1, column=3),
    'boiling_point': Label(info, image=images['boiling_point']).grid(row=1, column=4)
}
desc = Label(legende, image=images['legend']).pack()


class Atom:
    __column_limit, __row, __column = 18, 0, 0
    __labels = {
        'name': Label(info, text=""), 
        'amb_state': Label(info, text=""), 
        'fusion_point': Label(info, text=""), 
        'boiling_point': Label(info, text=""),
    }

    def __init__(self, dict):
        self.atom_info = {
            'name': dict['name'],
            'symbol': dict['symbol'],
            'atomic_num': dict['atomic_num'],
            'atomic_mass': dict['atomic_mass'],
            'amb_state': dict['amb_state'],
            'fusion_point': dict['fusion_point'],
            'boiling_point': dict['boiling_point'],
            'button': "b" + str(dict['atomic_num']),
            'image': PhotoImage(file="atomes/"+dict['symbol']+".PNG"),
        }
        self.__display_atoms()

    def __display_atoms(self):
        self.__button = Button(boutons, image=self.atom_info['image'], command=self.__display_infos).grid(row=self.__row, column=self.__column)
        Atom.__column += 1
        if Atom.__column >= Atom.__column_limit:
            Atom.__row += 1
            Atom.__column = 0

    def __display_infos(self):
        if self.atom_info['name'] != "":
            for label, i in zip(Atom.__labels.values(), (1, 2, 3, 4)):
                label.grid(row=2, column=i)
            for key, value in self.atom_info.items():
                try:
                    Atom.__labels[key].configure(text=value)
                except:
                    pass

    def create_blank(self, x):
        for i in range(x):
            self = Atom("", "vide", "", "", "", "", "")

with open('atomes.json', 'r') as file:
    atoms = loads(file.read())

for atom in atoms:
    atom['symbol'] = Atom(atom)

info.pack()
boutons.pack()
legende.pack()
root.mainloop()