{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNLiCLNuEp7j7eZPZc0Xibg",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/endtailer007/python-basics-assignment/blob/main/python-basics-assignment/python_basics_Sooraj.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Task 1**"
      ],
      "metadata": {
        "id": "Cpq2aNk3io_a"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "name=input(\"Enter your name: \")\n",
        "age=int(input(\"Enter your age: \"))\n",
        "height=float(input(\"Enter your height(cm): \"))\n",
        "is_student=input(\"Are you a student? (Yes/No): \")\n",
        "print(name,age,height,is_student)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aqutP-lmiuF6",
        "outputId": "22af9d5d-bd30-451c-b6b4-e723dfa632a4"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name: Sooraj\n",
            "Enter your age: 23\n",
            "Enter your height(cm): 168\n",
            "Are you a student? (Yes/No): No\n",
            "Sooraj 23 168.0 No\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Task 2**"
      ],
      "metadata": {
        "id": "f17CI6mokKgQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(f\"Name: {name} | Age: {age} | Height: {height} | Student: {is_student}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JfTkLQC7kPyG",
        "outputId": "6f64acd1-9ae8-4ccc-b2f4-95805e40bb5f"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Name: Sooraj | Age: 23 | Height: 168.0 | Student: No\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Task 3**"
      ],
      "metadata": {
        "id": "vX1XSGSFlD5U"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(f\"Age in months: {age*12}\")\n",
        "print(f\"Age in days: {age*365}\")\n",
        "print(f\"Reminder when age is divided by 7: {age%7}\")\n",
        "print(f\"Age raised to the power of 2: {age**2}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XvNcCaIulGTj",
        "outputId": "b943bb8b-cff9-47a8-a3a3-4549594a6ba2"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Age in months: 276\n",
            "Age in days: 8395\n",
            "Reminder when age is divided by 7: 2\n",
            "Age raised to the power of 2: 529\n"
          ]
        }
      ]
    }
  ]
}