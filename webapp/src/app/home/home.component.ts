import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Route, Router } from '@angular/router';
import { TransferService } from '../transfer.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  thisselected:any = null;
  postdata: any
  type :any
  value :any
  result:any





  constructor(private router:Router,private http: HttpClient,private transfer:TransferService) { 
    
    this.http.get("http://127.0.0.1:5003/get").subscribe((res)=>{
      console.log(res);
    });

  }

  onfileselected(event:any){
    console.log(event)
    this.thisselected=<File>event.target.files[0]

  }
 onupload(){
   const fd = new FormData();
    fd.append('file',this.thisselected,this.thisselected.name);
    this.http.post("http://127.0.0.1:5003/home",fd).subscribe((event)=>{
      console.log(event);
    }); 
  }

    onpredicit(){
     this. postdata={
        period:this.type,
        target:this.value
     };
  
      this.http.post("http://127.0.0.1:5003/val",this.postdata).subscribe((res:any)=>{
      console.log(res);
      this.result=res;
      this.transfer.setmessage(this.result)




    }); 
    console.log(this.type)
    console.log(this.value)
      
      }
      
      ngOnInit(): void {}

      
  

}
