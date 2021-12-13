import java.awt.*;
import java.awt.image.BufferedImage;

/**
 * @Description 通用工具类
 * @ClassName CommonUtil
 * @Author yanchengzhi
 * @date 2021.06.22 21:19
 */
public final class CommonUtil {

    /*
     * @description: 将字符串转换为BufferedImage对象
     * @param: [strs]
     * @return: java.awt.image.BufferedImage
     * @author: yanchengzhi
     * @date: 2021/6/22 21:20
     */
    public static BufferedImage createImage(String[] strs) {
        // 设置背景宽高
        int width = strs.length * 20, height = 10;
        BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        // 获取图形上下文对象
        Graphics graphics = image.getGraphics();
        // 填充
        graphics.fillRect(0, 0, width, height);
        // 设定字体大小及样式
//        graphics.setFont(new Font("微软雅黑", Font.BOLD,18));
        graphics.setFont(new Font("微软雅黑", Font.PLAIN, 18));
        // 字体颜色
        graphics.setColor(Color.BLACK);
        for (int i = 0; i < strs.length; i++) {
            // 描绘字符串
            graphics.drawString(strs[i], 10, (i + 1) * 20);
        }
        graphics.dispose();
        return image;
    }
}
