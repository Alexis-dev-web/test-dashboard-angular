import { Component, ViewChild, Input, OnInit, input } from '@angular/core';
import { MatCard, MatCardContent } from '@angular/material/card';
import {
  ApexChart,
  ApexTitleSubtitle,
  ApexAxisChartSeries,
  ChartComponent,
  ApexDataLabels,
  ApexPlotOptions,
  ApexYAxis,
  ApexLegend,
  ApexFill,
  ApexStroke,
  NgApexchartsModule,
} from 'ng-apexcharts';
import { InjuredProducts } from '../../../domain/model/injuredProducts.model';
import { Utils } from '../../../../core/utils';
import { colors } from '../../../../core/colors';

type ApexXAxis = {
  type?: 'category' | 'datetime' | 'numeric';
  categories?: any;
  labels?: {
    style?: {
      colors?: string | string[];
      fontSize?: string;
    };
  };
};

export type ChartOptions = {
  series: ApexAxisChartSeries;
  chart: ApexChart;
  dataLabels: ApexDataLabels;
  fill: ApexFill;
  plotOptions: ApexPlotOptions;
  yaxis: ApexYAxis;
  xaxis: ApexXAxis;
  colors: string[];
  legend: ApexLegend;
  title: ApexTitleSubtitle;
  stroke: ApexStroke;
};

@Component({
  selector: 'app-frecuency-inquire',
  standalone: true,
  imports: [
    MatCard,
    MatCardContent,
    NgApexchartsModule
  ],
  templateUrl: './frecuency-inquire.component.html',
  styleUrl: './frecuency-inquire.component.css',
})
export class FrecuencyInquireComponent implements OnInit {
  @Input() breakpoint!: number;
  @Input() products!: InjuredProducts[];
  @ViewChild('chart') chart!: ChartComponent;
  public chartOptions!: Partial<ChartOptions>;
  public colors: string[] = colors;
  public categories: string[] = [];
  public utils = new Utils()
  public values: number[] = [];

  constructor() {}

  ngOnInit(): void {
    this.utils.getColor(this.colors, this.products)
    this.products.map((product) => {
      this.values.push(product.averageDays)
      this.categories.push(product.name)
    })
    this.initChart()
  }

  initChart(): void {
    this.chartOptions = {
      series: [
        {
          name: 'Times',
          group: 'budget',
          data: this.values,
        },
      ],
      chart: {
        height: 350,
        type: 'bar',
        toolbar: {
          show: false,
        },
      },
      colors: this.colors,
      plotOptions: {
        bar: {
          columnWidth:
            this.breakpoint == 1 ? '20px' : '162px',
          distributed: true,
        },
      },
      dataLabels: {
        enabled: false,
      },
      legend: {
        show: true,
        position: 'top',
        horizontalAlign: 'left',
        markers: {
          offsetX: 155,
          width: 65,
          height: 5,
          radius: 5,
        },
      },
      title: {
        text: 'Frecuency of material inquire',
      },
      xaxis: {
        categories:this.categories,
        labels: {
          style: {
            colors: '#658398',
            fontSize: '10px',
          },
        },
      },
      stroke: {
        width: 2,
      },
      fill: {
        type: ['gradient'],
        gradient: {
          shade: 'light',
          type: 'vertical',
          shadeIntensity: 0.6,
          opacityFrom: 0.8,
          opacityTo: 0,
          stops: [0, 100],
        },
      },
      yaxis: {
        stepSize: 1,
        
      },
    };
  }
}
