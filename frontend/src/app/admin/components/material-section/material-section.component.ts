import { Component, Input, OnInit } from '@angular/core';
import { FrecuencyInquireComponent } from './frecuency-inquire/frecuency-inquire.component';
import { MatGridList } from '@angular/material/grid-list';
import { MatGridTile } from '@angular/material/grid-list';
import { CompletedAdvanceComponent } from './completed-advance/completed-advance.component';
import { InjuredProducts } from '../../domain/model/injuredProducts.model';
import { ProductProgress } from '../../domain/model/productProgress.model';
import { Utils } from '../../../core/utils';
import { colors, doubleColors } from '../../../core/colors';


@Component({
  selector: 'app-material-section',
  standalone: true,
  imports: [
    FrecuencyInquireComponent,
    MatGridList,
    MatGridTile,
    CompletedAdvanceComponent,
  ],
  templateUrl: './material-section.component.html',
  styleUrl: './material-section.component.css'
})

export class MaterialSectionComponent implements OnInit {
  @Input() breakpoint!: number;
  @Input() injuredProducts!: InjuredProducts[];
  @Input() productProgress!: ProductProgress[];
  public utils: Utils = new Utils()
  public newProducts: ProductProgress[] = [];
  
  constructor() {
  }
  ngOnInit(): void {
    let count = 1
    this.productProgress.map((product) => {
      product.color = this.utils.getColorByCount(doubleColors, count)
      this.newProducts.push(product)
      count += 1
    })
  }

  items = [
    {
      'backgroundColor': '#01A696',
      'trackColor': '#CAEEEB',
      'completed': 90,
      'adquired': 450
    },
    {
      'backgroundColor': '#1D4ED8',
      'trackColor': '#93C5FD',
      'completed': 220,
      'adquired': 500
    },
    {
      'backgroundColor': '#C2410C',
      'trackColor': '#FB923C',
      'completed': 300,
      'adquired': 450
    },
  ]
}
