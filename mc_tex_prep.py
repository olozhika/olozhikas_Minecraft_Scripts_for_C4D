import c4d

def remove_tex_prefix(texture_path):
    # 删掉Mineways引入的'./tex/'
    if './tex/' in texture_path:
        texture_path = texture_path.replace('./tex/', '')
    return texture_path

def main():
    # 获取当前文档
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        return

    # 获取场景中的所有材质球
    materials = doc.GetMaterials()

    # 遍历所有材质球
    for material in materials:
        # 颜色通道
        color_channel = material[c4d.MATERIAL_COLOR_SHADER]
        if color_channel and color_channel.CheckType(c4d.Xbitmap):
            # 修改颜色通道贴图的采样方式为"无"
            color_channel[c4d.BITMAPSHADER_INTERPOLATION] = 0
            # 删掉Mineways引入的'./tex/'
            texture_path = color_channel[c4d.BITMAPSHADER_FILENAME]
            new_texture_path = remove_tex_prefix(texture_path)
            color_channel[c4d.BITMAPSHADER_FILENAME] = new_texture_path

        # alpha通道
        alpha_channel = material[c4d.MATERIAL_ALPHA_SHADER]
        if alpha_channel and alpha_channel.CheckType(c4d.Xbitmap):
            # 修改alpha通道贴图的采样方式为"无"
            alpha_channel[c4d.BITMAPSHADER_INTERPOLATION] = 0
            # 删掉Mineways引入的'./tex/'
            texture_path = alpha_channel[c4d.BITMAPSHADER_FILENAME]
            new_texture_path = remove_tex_prefix(texture_path)
            alpha_channel[c4d.BITMAPSHADER_FILENAME] = new_texture_path

        # 关闭发光通道
        material[c4d.MATERIAL_USE_LUMINANCE] = False

    # 更新C4D界面
    c4d.EventAdd()

# 运行脚本
if __name__ == '__main__':
    main()
