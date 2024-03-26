# Minecraft Scripts for C4D

Some tiny Minecraft related scripts to inhance your wolkflow in C4D.

Put them in to your script folder to run.

Use your C4D interface to find the script folder: Scripts - User's scripts - Scripts folder

## Textures

### fix_c4d_texture.py

The script fixs texture paths and interpolations (from 'MIPS' to 'none'). 

It's for the original C4D textures.

Run it after importing your Minecraft .obj map.

### fix_rs_texture.py

The script fixs the filter methods of all your Redshift textures to 'none'. 

### rs_sss_setting.py

The script changes the sub-surface `scatter scale` and `phase` of all selected redshift materials to the values you want.

The values are 1.2 and 0.75 by default. 

Change the values at the line `change_sss_settings(mat, 1.2, 0.75) #CHANGE THE VALUES HERE!!! :D`

# Some CMD scripts
Some cmd scripts that may also help in inhancing your workflow of minecraft wallpapers.

### rename2png.py

The script add '.png' to all the files in a folder

it can be used to extract skins from servers in your `\.minecraft\assets\skins`

use it in cmd: `python rename2png.py yourfolder`
