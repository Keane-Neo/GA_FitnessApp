import express from "express";
import { signup, login } from "../controller/UserController.js";

const authRouter = express.Router();

authRouter.post("/signup", signup);
authRouter.post("/login", login);

export default authRouter;
