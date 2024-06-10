import { InjuredProducts } from '../../domain/model/injuredProducts.model';
import { InjuredProductDTO } from '../dto/injuredProducts.dto';

export class InjjuredProductMapper {
  static fromApiToDomain(products: InjuredProductDTO[]): InjuredProducts[] {
    var response: InjuredProducts[] = [];

    products.map((product) =>
      response.push({
        id: product.id,
        name: product.name,
        averageDays: product.average_days,
        color: undefined,
      })
    );
    return response;
  }
}
