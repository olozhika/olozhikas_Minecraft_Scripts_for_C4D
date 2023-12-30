import c4d
import redshift

def main():
    # 获取当前场景
    doc = c4d.documents.GetActiveDocument()

    # 获取场景中的所有材质
    materials = doc.GetMaterials()
    print(len(materials))
    for currentMat in materials:
        NodMaster = redshift.GetRSMaterialNodeMaster(currentMat)
        if NodMaster != None :
            rotShader = NodMaster.GetRoot()
            nodes = rotShader.GetChildren()
            for nod in nodes:
                nod[c4d.REDSHIFT_SHADER_TEXTURESAMPLER_FILTER_ENABLE_TYPE] = 0  # 0表示none
    # 更新场景
    c4d.EventAdd()

# 运行脚本
if __name__=='__main__':
    main()
