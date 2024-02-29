import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TransferService {
 message: any;
 
 setmessage(data:any){
  this.message=data;
 }
 getmessage(){
  return this.message;
 }

 

  constructor() { }
}
