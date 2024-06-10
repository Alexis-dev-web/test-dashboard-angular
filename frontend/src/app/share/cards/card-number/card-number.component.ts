import { Component, Input, TemplateRef } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { OrderStatusModel } from '../../../admin/domain/model/orderStatus.model';

@Component({
  selector: 'app-card-number',
  standalone: true,
  imports: [
    MatCardModule
  ],
  templateUrl: './card-number.component.html',
  styleUrl: './card-number.component.css'
})

export class CardNumberComponent {
  @Input() item!: OrderStatusModel
  @Input() textColor: string = 'gray'
  @Input() listRef!: TemplateRef<OrderStatusModel>
}
