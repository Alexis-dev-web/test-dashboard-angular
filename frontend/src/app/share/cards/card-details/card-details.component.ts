import { Component, Input } from '@angular/core';
import { MatCard } from '@angular/material/card';
import { MatCardContent } from '@angular/material/card';
import { MatCardTitle } from '@angular/material/card';
import { MatCardActions } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';


export type texts = {
  title: string,
  subtitle: string
}

@Component({
  selector: 'app-card-details',
  standalone: true,
  imports: [
    MatCard,
    MatCardActions,
    MatCardContent,
    MatCardTitle,
    MatButtonModule,
  ],
  templateUrl: './card-details.component.html',
  styleUrl: './card-details.component.css'
})

export class CardDetailsComponent {
  @Input() onClick!: Function
  @Input() backgroundColor!: string
  @Input() title!: string
  @Input() subtitle!: string
  @Input() content!: Node
  @Input() details!: string | number
  @Input() button!: string
  @Input() texts!: texts

  constructor() {}

}
