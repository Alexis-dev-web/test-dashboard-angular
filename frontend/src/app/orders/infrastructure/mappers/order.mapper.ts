import { DeliveredAddressMapper } from '../../../organization/infraestructure/mappers/deliveredAddress.mapper';
import { Order } from '../../domain/models/order.model';
import { OrderDTO } from '../dto/order.dto';

export class OrderMapper {
  static fromApiToDomain(order: OrderDTO): Order {
    return {
      id: order.id,
      deliveredAddressId: order.delivered_address_id,
      deliveredDate: order.delivered_date,
      deliveredOnTime: order.delivered_on_time,
      createdAt: order.created_at,
      updatedAt: order.updated_at,
      reasonCancelled: order.reason_cancelled,
      realDeliveredDate: order.real_delivered_date,
      deliveredTotalDays: order.delivered_total_days,
      number: order.number,
      quantity: order.quantity,
      totalPrice: order.total_price,
      providerId: order.provider_id,
      status: order.status,
      isActive: order.is_active,
      isPaid: order.is_paid,
      paidDate: order.paid_date,
      realPaidDate: order.real_paid_date,
      address: order.address ? DeliveredAddressMapper.fromApiToDomain(order.address!) : undefined,
    };
  }
}
