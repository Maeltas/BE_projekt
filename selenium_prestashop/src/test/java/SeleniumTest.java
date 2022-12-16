import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.assertEquals;

public class SeleniumTest {

    @Test
    public void componentTest() {

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--ignore-ssl-errors=yes");
        options.addArguments("--ignore-certificate-errors");
        Map<String, Object> prefs = new HashMap<String, Object>();
        prefs.put("credentials_enable_service", false);
        prefs.put("profile.password_manager_enabled", false);
        prefs.put("profile.address_manager_enabled", false);
        options.setExperimentalOption("prefs", prefs);
        WebDriver driver = new ChromeDriver(options);
        WebElement buttonToClick;
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofMillis(5000));
        driver.get("https://some_prestashop/");
        boolean title = true;
        buttonToClick = driver.findElement(By.cssSelector("[data-id-product='2']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[class='btn btn-touchspin js-touchspin bootstrap-touchspin-up']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[class='btn btn-primary add-to-cart']"));
        buttonToClick.click();
        wait.until(ExpectedConditions.presenceOfElementLocated(By.className("modal-dialog")));
        wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(".//button[@class='btn btn-secondary']")));
        buttonToClick = driver.findElement(By.xpath(".//button[@class='btn btn-secondary']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[href='https://some_prestashop/4-zasilacze']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[data-id-product='94']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[class='btn btn-primary add-to-cart']"));
        buttonToClick.click();
        wait.until(ExpectedConditions.presenceOfElementLocated(By.className("modal-dialog")));
        wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(".//button[@class='btn btn-secondary']")));
        buttonToClick = driver.findElement(By.xpath(".//button[@class='btn btn-secondary']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[href='https://some_prestashop/3-chlodzenie']"));
        buttonToClick.click();
//        buttonToClick = driver.findElement(By.cssSelector("[href='https://some_prestashop/brand/1-amd']"));
//        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[data-id-product='1']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[class='btn btn-touchspin js-touchspin bootstrap-touchspin-up']"));
        buttonToClick.click();
        buttonToClick.click();
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[class='btn btn-primary add-to-cart']"));
        buttonToClick.click();
        wait.until(ExpectedConditions.presenceOfElementLocated(By.className("modal-dialog")));
        wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(".//button[@class='btn btn-secondary']")));
        buttonToClick = driver.findElement(By.xpath(".//button[@class='btn btn-secondary']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[href='https://some_prestashop/5-karty-graficzne']"));
        buttonToClick.click();
//        buttonToClick = driver.findElement(By.cssSelector("[href='https://some_prestashop/brand/4-nvidia']"));
//        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[data-id-product='190']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[class='btn btn-touchspin js-touchspin bootstrap-touchspin-up']"));
        buttonToClick.click();
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[class='btn btn-primary add-to-cart']"));
        buttonToClick.click();
        wait.until(ExpectedConditions.presenceOfElementLocated(By.className("modal-dialog")));
        wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(".//button[@class='btn btn-secondary']")));
        buttonToClick = driver.findElement(By.xpath(".//button[@class='btn btn-secondary']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[href='//some_prestashop/koszyk?action=show']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("a[rel='nofollow'][href='https://some_prestashop/koszyk?delete=1&id_product=94&id_product_attribute=0&token=d362f4cca011fe6ac6677bce511c310b']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[href='https://some_prestashop/logowanie?back=https%3A%2F%2Fsome_prestashop%2Fkoszyk%3Faction%3Dshow'"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[href='https://some_prestashop/index.php?controller=registration']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("#field-id_gender-1"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("#field-firstname"));
        buttonToClick.sendKeys("Marcin");
        buttonToClick = driver.findElement(By.cssSelector("#field-lastname"));
        buttonToClick.sendKeys("Grzybek");
        buttonToClick = driver.findElement(By.cssSelector("#field-email"));
        buttonToClick.sendKeys("student@pg.pl");
        buttonToClick = driver.findElement(By.cssSelector("#field-password"));
        buttonToClick.sendKeys("Haslo1234@");
        buttonToClick = driver.findElement(By.cssSelector("input[value='1'][name='customer_privacy']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("button[type='submit']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[href='//some_prestashop/koszyk?action=show']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[href='https://some_prestashop/zamówienie']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("#field-address1"));
        buttonToClick.sendKeys("Narutowicza 11");
        buttonToClick = driver.findElement(By.cssSelector("#field-postcode"));
        buttonToClick.sendKeys("80-233");
        buttonToClick = driver.findElement(By.cssSelector("#field-city"));
        buttonToClick.sendKeys("Gdansk");
        buttonToClick = driver.findElement(By.cssSelector("[name='confirm-addresses']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[name='confirmDeliveryOption']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("#payment-option-2"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[id='conditions_to_approve[terms-and-conditions]']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.xpath(".//button[contains(text(),'Złóż zamówienie')]"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[href='https://some_prestashop/']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[href='https://some_prestashop/moje-konto']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector("[href='https://some_prestashop/historia-zamowien']"));
        buttonToClick.click();
        buttonToClick = driver.findElement(By.cssSelector(".view-order-details-link"));
        buttonToClick.click();


        assertEquals(true, title);


    }
}
