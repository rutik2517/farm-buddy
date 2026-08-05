#!C:\Python312\python.exe
import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Checkout</title>

<style>
body {
  font-family: Arial;
  background: #f5f5f5;
}

.checkout-container {
  width: 400px;
  margin: 50px auto;
  padding: 25px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.checkout-container h2 {
  text-align: center;
}

input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.row {
  display: flex;
  gap: 10px;
}

button {
  width: 100%;
  padding: 12px;
  background: green;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background: darkgreen;
}
</style>
</head>

<body>

<div class="checkout-container">
  <h2>Checkout</h2>

  <form id="checkoutForm">
    <input type="text" class="name" placeholder="Full Name">
    <input type="text" class="addr" placeholder="Address">
    <input type="number" class="phone" placeholder="Phone Number">
    <input type="text" class="card" placeholder="Card Number">

    
    <button type="button" id="btn">Place Order</button>
  </form>
</div>

<script type="module">
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.19.1/firebase-app.js";
import { getDatabase, ref, get, child, update } from "https://www.gstatic.com/firebasejs/9.19.1/firebase-database.js";

const firebaseConfig = {
  apiKey: "AIzaSyAYWp1h1C2AALmc39b6cqwv6GSqlWQrR1c",
  authDomain: "farmbuddy-106.firebaseapp.com",
  databaseURL: "https://farmbuddy-106-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "farmbuddy-106",
  storageBucket: "farmbuddy-106.appspot.com",
  messagingSenderId: "246405477593",
  appId: "1:246405477593:web:76c615bf7f242294317ac8"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase();

document.getElementById("btn").addEventListener("click", () => {

  const name = document.querySelector(".name").value;
  const addr = document.querySelector(".addr").value;
  const phone = document.querySelector(".phone").value;
  const card = document.querySelector(".card").value;
  const cvv = document.querySelector(".cvv").value;
  const exp = document.querySelector(".expiry").value;

  if (!name || !addr || !phone || !card || !cvv || !exp) {
    alert("Please fill all fields");
    return;
  }

  const dbref = ref(db);

  get(child(dbref, "user/" + name))
    .then((snapshot) => {
      if (snapshot.exists()) {

        let order = snapshot.val().orders || 0;

        update(child(dbref, "user/" + name), {
          Address: addr,
          Phone: phone,
          orders: order + 1
        });

        alert("Order Placed Successfully");
        window.location.href = "../Profile";

      } else {
        alert("User not found");
      }
    })
    .catch((error) => {
      alert(error);
    });

});
</script>

</body>
</html>
""")