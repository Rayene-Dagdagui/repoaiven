import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({ providedIn: 'root' })
export class SpesaService {
private x ="https://reimagined-space-spoon-7v79vvxv9vvpfr4jp-5000.app.github.dev/spesa";
constructor(private http: HttpClient) {}
getLista() {
return this.http.get(this.x);
}
aggiungiElemento(elemento: string) {
return this.http.post(this.x, { elemento });
}
}