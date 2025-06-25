from django.shortcuts import render
from .art import logo  # Assuming art.py contains the logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 2

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount)%26
            end_text += alphabet[new_position]
        else:
            end_text += char
    return end_text

def cipher_view(request):
    result = ""
    if request.method == "POST":
        direction = request.POST.get("direction")
        text = request.POST.get("text", "").lower()
        shift_raw=request.POST.get("shift","").strip()
        try:
            shift = int(shift_raw) % 26  # Handle large shifts
            result = caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        except ValueError:
            result = "Error: Shift must be a number."
    return render(request, "cipher/index.html", {"logo": logo, "result": result})