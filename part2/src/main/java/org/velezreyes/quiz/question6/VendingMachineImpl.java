package org.velezreyes.quiz.question6;

import java.util.ArrayList;
import java.util.List;

public class VendingMachineImpl implements VendingMachine {

  private static VendingMachineImpl instance = null;
  private double currentBalance = 0.0;
  private double costOfDrink = 0.75;


  private VendingMachineImpl() {
  }

  public static VendingMachine getInstance() {

    if (instance == null) {
      instance = new VendingMachineImpl();
    }

    return instance;
  }

  @Override
  public void insertQuarter() {
    currentBalance += 0.25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {

    //Comprobation current balance
    if (name.contains("Cola") && currentBalance < costOfDrink) {
        throw new NotEnoughMoneyException();
      
    } else if (name.contains("Tea") && currentBalance <= costOfDrink) {
        throw new NotEnoughMoneyException();

    }

    // Check that the drink is known
    if (name.contains("Cola") == false && name.contains("Tea") == false) {
      throw new UnknownDrinkException();
    }

 

    // Deduct the cost of the drink from the current balance
    currentBalance -= costOfDrink;

    // Return a new drink instance
    return new Drink() {
      @Override
      public String getName() {
        return name;
      }

      @Override
      public boolean isFizzy() {
        // Fizzy check
        return name.contains("Cola");
      }

    };
  }

}


