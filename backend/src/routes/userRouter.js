import express from "express";
import multer from "multer";
import {
  signup,
  showAll,
  showOne,
  showTrainers,
  update,
  login,
  updateTrainer,
} from "../controller/UserController.js";

const userRouter = express.Router();
const upload = multer();

userRouter.get("/", showAll);
userRouter.post("/signup", signup);
userRouter.post("/login", login);
userRouter.get("/trainers", showTrainers);
userRouter.get("/:id", showOne);
//Route to edit a trainer's clients list
userRouter.put("/trainer/:id", updateTrainer);

// Route to update user profile details
userRouter.put("/:id", upload.single("files"), update);

export default userRouter;
