from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox

# Create the window
window = Tk()
window.title("Pokemon Info")

# TODO: Additional window configuration
frm_top = ttk.Frame(window)
frm_top.grid(row=0, column=0, columnspan=2, pady=(20,10))

frm_btm_left = ttk.LabelFrame(window, text='Info')
frm_btm_left.grid(row=1, column=0, padx=(20,10), pady=(10, 20))

frm_btm_right = ttk.LabelFrame(window, text='Stats')
frm_btm_right.grid(row=1, column=1, padx=(10,20), pady=(10, 20))

# TODO: Add widgets to window
lbl_name = ttk.Label(frm_top, text='Pokemon Name:')
lbl_name.grid(row=0, column=0, padx=(10,5), pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

def handle_get_info():
    poke_name = ent_name.get().strip()
    if len(poke_name) == 0:
        return

    poke_info = get_pokemon_info(poke_name)
    if poke_info is None:
        error_msg = f'Unable to fetch information for {poke_name.capitalize()} from the PokeAPI.'
        messagebox.showinfo(title='Error', message=error_msg, icon='error')

    lbl_height_value['text'] = f"{poke_info['height']} dm"
    lbl_weight_value['text'] = f"{poke_info['weight']} kg"

    types = ", ".join([t['type']['name'] for t in poke_info['types']])
    lbl_type_value['text'] = types

    bar_hp['value'] = poke_info['stats'][0]['base_stat']
    bar_attack['value'] = poke_info['stats'][1]['base_stat']
    bar_defense['value'] = poke_info['stats'][2]['base_stat']
    bar_Special_Attack['value'] = poke_info['stats'][3]['base_stat']
    bar_Special_Defense['value'] = poke_info['stats'][4]['base_stat']
    bar_Speed['value'] = poke_info['stats'][5]['base_stat']

    return


btn_grt_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info)
btn_grt_info.grid(row=0, column=2, padx=10, pady=10)

#

lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=E)

lbl_height_value = ttk.Label(frm_btm_left, text='TBD')
lbl_height_value.grid(row=0, column=1, padx=(0,10), pady=(10,5), sticky=E)

lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, padx=(10,5), pady=(10,5), sticky=E)

lbl_weight_value = ttk.Label(frm_btm_left, text='')
lbl_weight_value.grid(row=1, column=1, padx=(0,10), pady=(10,5), sticky=E)

lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, padx=(10,5), pady=(10,5), sticky=E)

lbl_type_value = ttk.Label(frm_btm_left, text='')
lbl_type_value.grid(row=2, column=1, padx=(0,10), pady=(10,5), sticky=E)

#

lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, sticky=E, padx=(10,5), pady=(10,5))
bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_hp.grid(row=0, column=1)

lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, sticky=E, padx=(10,5), pady=5)
bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_attack.grid(row=1, column=1)

lbl_defense = ttk.Label(frm_btm_right, text='Defense:')
lbl_defense.grid(row=2, column=0, sticky=E, padx=(10,5), pady=5)
bar_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_defense.grid(row=2, column=1)

lbl_Special_Attack = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_Special_Attack.grid(row=3, column=0, sticky=E, padx=(10,5), pady=5)
bar_Special_Attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_Special_Attack.grid(row=3, column=1)

lbl_Special_Defense= ttk.Label(frm_btm_right, text='Special Defense:')
lbl_Special_Defense.grid(row=4, column=0, sticky=E, padx=(10,5), pady=5)
bar_Special_Defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_Special_Defense.grid(row=4, column=1)

lbl_Speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_Speed.grid(row=5, column=0, sticky=E, padx=(10,5), pady=5)
bar_Speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_Speed.grid(row=5, column=1)
# Loop until window is closed


window.mainloop()
