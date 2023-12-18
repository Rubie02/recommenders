import asyncio
import tornado.web
from surprise.dump import load
from collections import defaultdict

class MainHandler(tornado.web.RequestHandler):
    def get(self, user_id):
        dump_path = 'model/best_model.pkl'
        n = 8
        svdpp = load(dump_path)[1]
        
        top_n = defaultdict(dict)

        for uid, iid, true_r, est, _ in svdpp:
            top_n[uid][iid] = est
        
        for uid, user_ratings in top_n.items():
            sorted_ratings = dict(sorted(user_ratings.items(), key=lambda item: item[1], reverse=True))
            top_n[uid] = dict(list(sorted_ratings.items())[:n])


        self.write(top_n.get(user_id))

def make_app():
    return tornado.web.Application([
        (r"/recommenders/([^/]+)", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())