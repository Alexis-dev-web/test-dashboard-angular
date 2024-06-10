import { Component, Input, OnInit } from '@angular/core';
import { TransitChartComponent } from './transit-chart/transit-chart.component';
import { MatGridList } from '@angular/material/grid-list';
import { MatGridTile } from '@angular/material/grid-list';
import { CardDetailsComponent } from '../../../share/cards/card-details/card-details.component';
import { Order } from '../../../orders/domain/models/order.model';
import { OrderByYear } from '../../domain/model/orderByYear.model';
import { MatCard, MatCardContent } from '@angular/material/card';

@Component({
  selector: 'app-delivery-section',
  standalone: true,
  imports: [
    CardDetailsComponent,
    TransitChartComponent,
    MatGridList, 
    MatGridTile,
    MatCard,
    MatCardContent,
  ],
  templateUrl: './delivery-section.component.html',
  styleUrl: './delivery-section.component.css'
})
export class DeliverySectionComponent implements OnInit{
  @Input() breakpoint!: number;
  @Input() nextPayment!: Order;
  @Input() nextDelivered!: Order;
  @Input() ordersByYear!: OrderByYear[]
  days!: number
  day!: number
  month!: number
  daysNextPayment!: number

  constructor() {}
  
  ngOnInit(): void {
    const deliveredDate: any = new Date(this.nextDelivered.deliveredDate)
    const nextPaymentDate: any = new Date(this.nextPayment.paidDate)
    const today: any = new Date()
  
    let diff = Math.abs((nextPaymentDate - today))
    let diiffNextPayment =  Math.abs((deliveredDate - today))
    this.days = Math.floor(diff / (1000 * 60 * 60 * 24));
    this.day = deliveredDate.getDay()
    this.month = deliveredDate.getMonth() + 1
    this.daysNextPayment = Math.floor(diiffNextPayment / (1000 * 60 * 60 * 24));
  }
}
