document.addEventListener("keydown", (e) => {
    const key = e.key.toLowerCase();

    if (["w", "a", "s", "d"].includes(key)) {
        console.log("Move:", key);
    }

    if (key === "h") {
        console.log("High step mode");
    }

    if (key === "l") {
        console.log("Low step mode");
    }
});
