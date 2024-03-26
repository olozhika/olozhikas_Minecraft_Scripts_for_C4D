import c4d
import redshift

# Function to change the SSS settings of Redshift materials
def change_sss_settings(material, scatter_scale, phase_value):
    # Check if the material is a Redshift material
    if 1:
        NodMaster = redshift.GetRSMaterialNodeMaster(material)
        if NodMaster != None :
            rotShader = NodMaster.GetRoot()
            nodes = rotShader.GetChildren()
            for nod in nodes:
               nod[c4d.REDSHIFT_SHADER_MATERIAL_SS_AMOUNT] = scatter_scale
               nod[c4d.REDSHIFT_SHADER_MATERIAL_SS_PHASE] = phase_value

def main():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()
    
    # Start undo action
    doc.StartUndo()
    
    # Check if any materials are selected
    selected_materials = doc.GetActiveMaterials()
    
    if selected_materials:
        # Loop through the selected materials
        for mat in selected_materials:
            # Change the SSS settings
            change_sss_settings(mat, 1.2, 0.75) #CHANGE THE VALUES HERE!!! :D
            # Add undo command for changing the material
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, mat)
    
    # End undo action
    doc.EndUndo()
    
    # Inform Cinema 4D of the changes
    c4d.EventAdd()

# Execute main function
if __name__=='__main__':
    main()
