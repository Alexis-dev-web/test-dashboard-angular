import { OrderMapper } from '../../../orders/infrastructure/mappers/order.mapper';
import { InjuredProducts } from '../../domain/model/injuredProducts.model';
import { OrderReport } from '../../domain/model/reportOrder.model';
import { ReportOrdersDTO } from '../dto/reportOrders.dto';
import { InjjuredProductMapper } from './injuredProductMapper';
import { OrderByYearMapper } from './orderByYear.mapper';
import { OrderStatusMapper } from './orderStatus.mapper';
import { ProductProgressMapper } from './productProgress.mapper';
import { ProviderDeliveredMapper } from './providerDelivered.mapper';

export class OrderReportMapper {
  static fromApiToDomain(report: ReportOrdersDTO): OrderReport {
    
    return {
      nextOrderPaid: OrderMapper.fromApiToDomain(report.next_order_paid),
      nextOrderDelivered: OrderMapper.fromApiToDomain(
        report.next_order_delivered
      ),
      status: OrderStatusMapper.fromApiToDomain(report.status),
      ordersDeliveredOnTime: report.orders_delivered_on_time,
      orderNotDelivered: report.order_not_delivered,
      totalQuantity: report.total_quantity,
      totalCost: report.total_cost,
      ordersByYear: OrderByYearMapper.fromApiToDomain(report.orders_by_year),
      averageDelivered: report.average_delivered,
      productProgress: report.product_progress ? ProductProgressMapper.fromApiToDomain(report.product_progress) : [],
      providerDelivery: report.provider_delivery ? ProviderDeliveredMapper.fromApiToDomain(report.provider_delivery) : [],
      injuredProducts: report.injured_products ? InjjuredProductMapper.fromApiToDomain(report.injured_products) : []
    };
  }
}
