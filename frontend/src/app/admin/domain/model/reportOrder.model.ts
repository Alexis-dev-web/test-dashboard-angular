import { Order } from '../../../orders/domain/models/order.model';
import { InjuredProducts } from './injuredProducts.model';
import { OrderByYear } from './orderByYear.model';
import { OrderStatusModel } from './orderStatus.model';
import { ProductProgress } from './productProgress.model';
import { ProviderDelivered } from './providerDelivered.model';

export class OrderReport {
  constructor(
    public nextOrderPaid: Order,
    public nextOrderDelivered: Order,
    public status: OrderStatusModel[],
    public ordersDeliveredOnTime: number,
    public orderNotDelivered: number,
    public totalQuantity: number,
    public totalCost: number,
    public ordersByYear: OrderByYear[],
    public averageDelivered: number,
    public productProgress?: ProductProgress[],
    public injuredProducts?: InjuredProducts[],
    public providerDelivery?: ProviderDelivered[],
  ) {}
}
