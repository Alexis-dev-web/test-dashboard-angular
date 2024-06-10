import { OrderStatus } from "../../../orders/infrastructure/dto/order.dto";
import { OrderReportStatus, OrderStatusModel } from "../../domain/model/orderStatus.model";
import { OrderStatusDTO } from "../dto/orderStatus.dto";

export class OrderStatusMapper {
  static fromApiToDomain(orderStatus: OrderStatusDTO): OrderStatusModel[] {
    let status = [
      new OrderStatusModel('#F97316', OrderReportStatus.ACTIVE, orderStatus.active),
      new OrderStatusModel('#01A696', OrderReportStatus.DELIVERED, orderStatus.delivered),
      new OrderStatusModel('#DC2626', OrderReportStatus.CANCELLED, orderStatus.cancelled)
    ]
  
    return status
  }
}