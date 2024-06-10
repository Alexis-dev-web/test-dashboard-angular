import { ProductProgress } from '../../domain/model/productProgress.model';
import { ProductProgressDTO } from '../dto/productProgress.dto';

export class ProductProgressMapper {
  static fromApiToDomain(products: ProductProgressDTO[]): ProductProgress[] {
    var product_progrees: ProductProgress[] = [];

    products.map((product) =>
      product_progrees.push({
        id: product.id,
        name: product.name,
        total_progress: product.total_progress,
        objective: product.objective,
        color: undefined,
      })
    );

    return product_progrees;
  }
}
