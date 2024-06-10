import { Component, OnInit, VERSION } from '@angular/core';
import { OrdersSectionComponent } from './components/orders-section/orders-section.component';
import { DeliverySectionComponent } from './components/delivery-section/delivery-section.component';
import { MaterialSectionComponent } from './components/material-section/material-section.component';
import { GetOrderReport } from './domain/useCases/get_orders.usecase';
import { OrderReport } from './domain/model/reportOrder.model';
import { FinancialSectionComponent } from './components/financial-section/financial-section.component';
import {
  OrderReportStatus,
  OrderStatusModel,
} from './domain/model/orderStatus.model';

@Component({
  selector: 'app-admin',
  standalone: true,
  imports: [
    FinancialSectionComponent,
    OrdersSectionComponent,
    DeliverySectionComponent,
    MaterialSectionComponent,
  ],
  templateUrl: './admin.component.html',
  styleUrl: './admin.component.css',
})
export class AdminComponent implements OnInit {
  ngVersion: string = VERSION.full;
  breakpoint!: number;
  report!: OrderReport;
  averageDelivered!: number;

  constructor(private getOrderReportUseCase: GetOrderReport) {}

  ngOnInit() {
    this.breakpoint =
      window.innerWidth <= 580 ? 1 : window.innerWidth <= 768 ? 2 : 4;
    this.getOrdersReport()
    
  }

  getOrdersReport(): void {
    this.getOrderReportUseCase.run().subscribe({
      next: (reportOrder: OrderReport) => {
        let total: number = 0;
        reportOrder.status.map((status) => {
          total += status.total;
        });
        reportOrder.status.unshift(
          new OrderStatusModel('grey', OrderReportStatus.TOTAL, total)
        );
        
        this.averageDelivered = this.getAverage(reportOrder.ordersDeliveredOnTime, reportOrder.orderNotDelivered)

        this.report = reportOrder
      },
      error: (error) => {
        console.error('Error al cargar las tareas:', error);
      },
    });
  }
  onResize(event: any) {
    this.breakpoint =
      event.target.innerWidth <= 580 ? 1 : window.innerWidth <= 768 ? 2 : 4;
    localStorage.setItem('breakpoint', this.breakpoint.toString());
  }

  getAverage(delivered: number, notDelivered: number): number {
    let total = delivered + notDelivered

    return (delivered * 100) / total
  }
}
