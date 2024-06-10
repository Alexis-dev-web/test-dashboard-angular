import { DoubleColors } from "./models/double_colors_model";

export class Utils {
  getColor(colors: any[], values: any[]) : any[] {
    let response: any[] = []
    let count = values.length;

   if (colors.length === values.length) {
    return colors
   }
    do {
      if (count > colors.length) {
        response.push(colors[values.length - count])
      } else {
        response.push(colors[count - 1])
      }
      count -= 1
    } while (count > 0)

      return response
  }

  getColorByCount(colors: any[], count: number) : DoubleColors {
    if (count > colors.length) {
      return colors[(count - colors.length) - 1]
    }

      return colors[count - 1]
  }
}

