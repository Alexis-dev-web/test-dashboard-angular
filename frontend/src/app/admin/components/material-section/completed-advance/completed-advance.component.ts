import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { MatCard, MatCardContent, MatCardTitle } from '@angular/material/card';
import { MatGridList, MatGridTile } from '@angular/material/grid-list';
import {MatDividerModule} from '@angular/material/divider';
import {MatListModule} from '@angular/material/list';

import {
  ApexNonAxisChartSeries,
  ApexPlotOptions,
  ApexChart,
  NgApexchartsModule,
  ChartComponent,
  ApexDataLabels,
  ApexLegend,
  ApexFill,
} from 'ng-apexcharts';

export type ChartOptions = {
  series: ApexNonAxisChartSeries;
  chart: ApexChart;
  dataLabels: ApexDataLabels;
  plotOptions: ApexPlotOptions;
  legend: ApexLegend;
  labels: string[];
  fill: ApexFill;
};

@Component({
  selector: 'app-completed-advance',
  standalone: true,
  imports: [
    MatCard,
    MatCardTitle,
    MatCardContent,
    NgApexchartsModule,
    MatGridList,
    MatGridTile,
    MatDividerModule,
    MatListModule
  ],
  templateUrl: './completed-advance.component.html',
  styleUrl: './completed-advance.component.css',
})
export class CompletedAdvanceComponent implements OnInit {
  @ViewChild('chart') chart!: ChartComponent;
  public chartOptions!: Partial<ChartOptions>;
  @Input() completed!: number;
  @Input() adquired!: number;
  @Input() backgroundColor!: string;
  @Input() trackColor!: string;
  porcentageAdvance!: number;

  constructor() {}
  ngOnInit(): void {
    this.initChar()
  }

  initChar(): void {
    this.porcentageAdvance = (this.completed * 100) / this.adquired

    this.chartOptions = {
      series: [this.porcentageAdvance],
      chart: {
        height: 180,
        type: 'radialBar',
      },
      fill: {
        colors: [this.backgroundColor],
      },
      plotOptions: {
        radialBar: {
          hollow: {
            margin: 0,
            size: '70%',
            background: '#fff',
            image: undefined,
          },
          track: {
            background: this.trackColor,
            margin: 0, // margin is in pixels
          },

          dataLabels: {
            show: false,
          },
        },
      },
    };
  }
}
