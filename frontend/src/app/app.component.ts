import { Component } from "@angular/core";
import { Subscription } from "rxjs";
import { ExamsApiService } from "./exams/exam-api.service";
import { Exam } from "./exams/exam.model";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"],
})
export class AppComponent {
  title = "frontend";
  examListSubscription: Subscription;
  examList: Exam[];

  constructor(private examApi: ExamsApiService) {}

  ngOnInit(): void {
    this.examListSubscription = this.examApi.getExams().subscribe((res) => {
      this.examList = res;
    }, console.error);
  }

  ngOnDestroy(): void {
    this.examListSubscription.unsubscribe();
  }
}
