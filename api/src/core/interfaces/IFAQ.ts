export interface ICategory {
  id: string;
  name: string;
}

export interface IFAQQuestion {
  id: number;
  question: string;
}

export interface IFAQ {
  id: number;
  question: string;
  answer: string;
  category: string;
}

export interface IFAQValidate {
  id?: number;
  question?: string;
}
