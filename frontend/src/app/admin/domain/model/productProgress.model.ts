import { DoubleColors } from "../../../core/models/double_colors_model";

export class ProductProgress {
  constructor(
    public id: string,
    public name: string,
    public total_progress: number,
    public objective: number,
    public color?: DoubleColors
  ) {}
}