import java.util.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;


public class ManagmentAction {
    
    // Check your balance
    // Make a deposit
    // Make a withdrawal
    // View the previous transaction
    // Calculate Interest
    // Exit the application

    public int totalMoney = 0;
    public ArrayList<Integer> transactionLog = new ArrayList<Integer>();
    public ArrayList<Integer> sendMoneyLog = new ArrayList<Integer>();
    public ArrayList<String> sendMoneyUserName = new ArrayList<String>();
    public ArrayList<String> depositWithdrawTimeLog = new ArrayList<String>();


    public void welcomingDisplay() {

        System.out.println("1. Check your balance");
        System.out.println("2. Make a deposit");
        System.out.println("3. Make a withdrawal");
        System.out.println("4. View the previous transaction");
        System.out.println("5. Send Money ");
        System.out.println("6. View the previous send money transaction");
        System.out.println("7. Exit the application");
        
        
        Scanner in = new Scanner(System.in);
        int displayChoice = in.nextInt();

        if (displayChoice == 1)
            checkBalance();
        else if (displayChoice == 2)
            deposit();
        else if (displayChoice == 3)
            withdrawal();
        else if (displayChoice == 4)
            recordTransaction();
        else if (displayChoice == 5)
            sendMoney();
        else if (displayChoice == 6)
            printingSendMoneyTransaction();
        else if (displayChoice == 7)
            interestCount();
        // else  
        //     exit();

    }


    // checking current balance
    public void checkBalance() {
        System.out.println("You currently have " + this.totalMoney + "$");

        
        System.out.println();
        welcomingDisplay();
    }


    // add deposit amount to total amount
    public void deposit() {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter deposit amount : ");
        int moneyDeposit = in.nextInt();
        this.totalMoney += moneyDeposit;
        this.transactionLog.add(moneyDeposit);
        this.depositWithdrawTimeLog.add(recordTimeLog());

        System.out.println();
        welcomingDisplay();
    }


    // minus withdrawal amount from total amount
    public void withdrawal() {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter withdrawal amount : ");
        int moneyWithdrawal = in.nextInt();
        this.totalMoney -= moneyWithdrawal;
        this.transactionLog.add(-moneyWithdrawal);
        this.depositWithdrawTimeLog.add(recordTimeLog());

        
        System.out.println();
        welcomingDisplay();
    }

    
    // record all send money transaction
    public void sendMoney() {
        Scanner in = new Scanner(System.in);
        
        System.out.println("Sender name : ");
        String userName = in.nextLine();

        System.out.println("Amount : ");
        int sendMoneyAmount = in.nextInt();
        if (this.totalMoney >= sendMoneyAmount) {
            this.totalMoney -= sendMoneyAmount;
            this.sendMoneyLog.add(sendMoneyAmount);
            this.sendMoneyUserName.add(userName);

            System.out.println();
            welcomingDisplay();
        }
        else
            System.out.println("Not enough money to send.");

        System.out.println();
        welcomingDisplay();
    }

    // print all send money transaction
    public void printingSendMoneyTransaction() {
        for (String name : sendMoneyUserName) {
            System.out.print(name);
            for (int money : transactionLog) {
                System.out.print(money);
            }
        }
    }


    // record all transaction
    public void recordTransaction() {
        for (String gettime : this.depositWithdrawTimeLog) {
            for (int i : this.transactionLog) {
                System.out.print(i + " > " + gettime);
            }
            System.out.println();
        }

        
        System.out.println();
        welcomingDisplay();

    }


    // count compound interest
    public void interestCount() {
        Scanner in = new Scanner(System.in);

        System.out.println("Amount : ");
        int principalAmount = in.nextInt();

        System.out.println("Interest rate : ");
        int annualInterest = in.nextInt();
        double makeflaotingNumberInterest = (double) annualInterest/100;

        System.out.println("Year : ");
        int numberOfYear = in.nextInt();
        
        double result = Math.pow(principalAmount*(1+makeflaotingNumberInterest), numberOfYear)-principalAmount;
        System.out.println("Interest will be " + result);


        
        System.out.println();
        welcomingDisplay();
    }



    public String recordTimeLog() {
        LocalDateTime myDateObj = LocalDateTime.now();
        DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm");

        String formattedDate = myDateObj.format(myFormatObj);
        return formattedDate;
    }






















}
