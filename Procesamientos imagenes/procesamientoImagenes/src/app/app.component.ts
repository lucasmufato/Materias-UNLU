import {Component, ElementRef, ViewChild} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  imagen: any;
  imagenOriginal;
  @ViewChild('original') canvasOriginal:ElementRef;
  canvasOriginalContext:CanvasRenderingContext2D;


  cargoImagen(event:any){
    console.log(event);
    console.log(event.srcElement);
    this.imagenOriginal = new Image();
    this.imagenOriginal.src = URL.createObjectURL(event.srcElement.files[0]);

    this.draw();
  }

  draw() {
    // this.canvasOriginal.width = 300;
    // this.canvasOriginal.height = 600;
    console.log(this.canvasOriginal);
    // let ctx = this.canvasOriginal.nativeElement.getContext('2d');
    this.canvasOriginalContext.drawImage(this.imagen, 0,0);
  }

  ngAfterViewInit(): void {
    this.canvasOriginalContext = (<HTMLCanvasElement>this.canvasOriginal.nativeElement).getContext('2d');
  }


}
