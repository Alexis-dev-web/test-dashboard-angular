import { Component, Input } from '@angular/core';
import { FinancialDataComponent } from './financial-data/financial-data.component';

@Component({
  selector: 'app-financial-section',
  standalone: true,
  imports: [FinancialDataComponent],
  templateUrl: './financial-section.component.html',
  styleUrl: './financial-section.component.css'
})
export class FinancialSectionComponent {
  @Input() breakpoint!: number;
}
