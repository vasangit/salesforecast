import { Component, OnInit } from '@angular/core';
import { ChartData } from 'chart.js';
import { Chart, registerables } from 'chart.js';
import { ChartOptions, ChartType, ChartDataset } from 'chart.js';
import { Color } from 'ng2-charts';
import { Route, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

import { TransferService } from '../transfer.service';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {



  date :any;
  value:any
  chart:any =[]
  result:any

  

  constructor(private http: HttpClient,private transfer: TransferService) { 
    Chart.register(...registerables); 
  }


  ngOnInit(): void {

    this.result=this.transfer.getmessage()
    console.log(this.result)

   
    const error1: any = document.getElementById('accuracy')
    error1.innerHTML=0.78;
    

    const error2: any = document.getElementById('mean')
    error2.innerHTML=1.544 ;


    // line chart 
    const lineCanvasEle: any = document.getElementById('line_chart')
    const lineChar = new Chart(lineCanvasEle.getContext('2d'), {
      type: 'line',
        data: {
          labels: this.result.period,
          datasets: [
            { data: this.result.target,
               label: 'Forecast Projection', 
               borderColor: 'rgba(54, 162, 235)' },

          ],
        },
        options: {
          responsive: true,
          scales: {
              y: {
                  
                  beginAtZero: true
              }
          }
        }
      });
   // Bar chart
      const barCanvasEle: any = document.getElementById('bar_chart')
      const barChart = new Chart(barCanvasEle.getContext('2d'), {
        type: 'bar',
          data: {
            labels: this.result.period,
            datasets: [{
              label: 'Sales',
              data: this.result.target,
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
              ],
              borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
              ],
              borderWidth: 1
            }]
          },
          options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
          }
        });

          
        
        
  }
  }
