//STONE PAPER SCISSOR GAME 
import java.util.*;
class Stone_paper
{
public static void main(String args[])
{
  int computer_choice,user_choice;
  System.out.println("0-rock ,1-paper ,2-scissor");
  Scanner sc=new Scanner(System.in);
  System.out.println("enter your choice:");
  user_choice=sc.nextInt();
  //computer's input
  Random random=new Random();
  computer_choice=random.nextInt(3);
  System.out.println("computer's choice:"+computer_choice);
  
  if(user_choice==computer_choice)
  {
  System.out.println("DRAW");
  }
  else if((user_choice==0 && computer_choice==2)||(user_choice==1 && computer_choice==0) ||(user_choice==2 &&computer_choice==1))
  {
  System.out.println("YOU WON");
  }
  else
  {
  System.out.println("YOU LOSE");
  }
 }
}
  