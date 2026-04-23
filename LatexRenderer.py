import io

from PyQt6.QtGui import QPixmap
from matplotlib import pyplot as plt


class LatexRenderer:
    def __init__(self):
        self.cachedPixmaps = {}

    def latexToPixmap(self, latex, fontSize=8, dpi=100):
        key = latex, fontSize, dpi
        if key in self.cachedPixmaps:
            return self.cachedPixmaps[key]
        pixmap = self.renderLatexToPixmap(latex, fontSize, dpi)
        self.cachedPixmaps[key] = pixmap
        return pixmap

    def renderLatexToPixmap(cls, latex, fontSize=8, dpi=100):
        # 初始创建图形，使用稍大的临时尺寸
        fig = plt.figure(figsize=(1, 1))
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')
        cleanTex = latex.strip('$')
        text_obj = ax.text(0.5, 0.5, f'${cleanTex}$', ha='center', va='center',
                           fontsize=fontSize, usetex=True)

        # 强制绘制以获取正确的渲染信息
        fig.canvas.draw()

        # 获取渲染后的边界框（在显示坐标中）
        renderer = fig.canvas.get_renderer()
        bbox = text_obj.get_window_extent(renderer)

        # 转换到英寸坐标，并添加额外的边距
        bbox_inches = bbox.transformed(fig.dpi_scale_trans.inverted())

        # 为可能被裁剪的部分添加边距（特别是上标和下标）
        padding = 0.1  # 增加10%的边距
        width = bbox_inches.width * (1 + padding)
        height = bbox_inches.height * (1 + padding)

        # 重新设置图形尺寸
        fig.set_size_inches(width, height)

        # 保存为PNG
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=dpi, bbox_inches='tight',
                    pad_inches=0.05, transparent=True)
        buf.seek(0)
        plt.close(fig)

        pixmap = QPixmap()
        pixmap.loadFromData(buf.getvalue())
        return pixmap


latexRenderer = LatexRenderer()
