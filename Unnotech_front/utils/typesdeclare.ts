interface NewsPhoto {
    imgUrl: string;
    comment: string;
}
export interface News {
    id: number;
    title: string;
    news_photo: Array<NewsPhoto>;
}
export interface NewsDetail extends News {
    author: string;
    paper: string;
    url: URL;
    content: string;
}
