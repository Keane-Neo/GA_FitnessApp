import express from "express";
import * as postController from "../controller/postController.js";

const postRouter = express.Router();

// Route to add a post
postRouter.post("/", postController.create);

// Route to get all posts. Need to receive specific user id inside request body
postRouter.get("/", postController.index);

// Route to get a specific post
postRouter.get("/:id", postController.show);

// Route to delete a specific post
postRouter.delete("/:id", postController.deletePost);

export default postRouter;