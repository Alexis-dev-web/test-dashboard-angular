import { OrderDTO } from '../../../orders/infrastructure/dto/order.dto';
import { InjuredProductDTO } from './injuredProducts.dto';
import { OrderByYearDTO } from './orderByYear.dto';
import { OrderStatusDTO } from './orderStatus.dto';
import { ProductProgressDTO } from './productProgress.dto';
import { ProviderDeliveredDTO } from './providerDelivered.dto';

export interface ReportOrdersDTO {
  next_order_paid: OrderDTO;
  next_order_delivered: OrderDTO;
  status: OrderStatusDTO;
  orders_delivered_on_time: number;
  order_not_delivered: number;
  total_quantity: number;
  total_cost: number;
  orders_by_year: OrderByYearDTO[];
  average_delivered: number;
  product_progress?: ProductProgressDTO[];
  injured_products?: InjuredProductDTO[];
  provider_delivery?: ProviderDeliveredDTO[];
}
