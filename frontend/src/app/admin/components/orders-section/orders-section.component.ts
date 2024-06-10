import { Component, Input } from '@angular/core';
import { MatGridList } from '@angular/material/grid-list';
import { MatGridTile } from '@angular/material/grid-list';
import { MatCard } from '@angular/material/card';
import { MatCardContent } from '@angular/material/card';
import { MatCardTitle } from '@angular/material/card';

import { CardNumberComponent } from '../../../share/cards/card-number/card-number.component';
import { OrderStatusModel } from '../../domain/model/orderStatus.model';

@Component({
  selector: 'app-orders-section',
  standalone: true,
  imports: [
    CardNumberComponent,
    MatGridList,
    MatGridTile,
    MatCard,
    MatCardContent,
    MatCardTitle,
  ],
  templateUrl: './orders-section.component.html',
  styleUrl: './orders-section.component.css'
})
export class OrdersSectionComponent {
  @Input() breakpoint!: number;
  @Input() totalSpend!: number;
  @Input() averageDelivered!: number;
  @Input() totalQuantity!: number;
  @Input() values!: OrderStatusModel[];
  @Input() averageDeliveredDays!: number;
}
