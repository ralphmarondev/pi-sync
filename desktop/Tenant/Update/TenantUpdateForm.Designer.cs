namespace PiSync.Tenant.Update
{
    partial class TenantUpdateForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            tbFingerprint = new ComboBox();
            tbGender = new ComboBox();
            btnUpdate = new Button();
            label7 = new Label();
            label8 = new Label();
            tbRegisteredDoors = new TextBox();
            label5 = new Label();
            tbPasswordHint = new TextBox();
            label6 = new Label();
            tbPassword = new TextBox();
            label3 = new Label();
            label4 = new Label();
            tbUsername = new TextBox();
            label2 = new Label();
            tbLastName = new TextBox();
            label1 = new Label();
            tbFirstName = new TextBox();
            label10 = new Label();
            tbEmail = new TextBox();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = SystemColors.Control;
            panel1.Controls.Add(label10);
            panel1.Controls.Add(tbEmail);
            panel1.Controls.Add(tbFingerprint);
            panel1.Controls.Add(tbGender);
            panel1.Controls.Add(btnUpdate);
            panel1.Controls.Add(label7);
            panel1.Controls.Add(label8);
            panel1.Controls.Add(tbRegisteredDoors);
            panel1.Controls.Add(label5);
            panel1.Controls.Add(tbPasswordHint);
            panel1.Controls.Add(label6);
            panel1.Controls.Add(tbPassword);
            panel1.Controls.Add(label3);
            panel1.Controls.Add(label4);
            panel1.Controls.Add(tbUsername);
            panel1.Controls.Add(label2);
            panel1.Controls.Add(tbLastName);
            panel1.Controls.Add(label1);
            panel1.Controls.Add(tbFirstName);
            panel1.Location = new Point(42, 24);
            panel1.Name = "panel1";
            panel1.Size = new Size(694, 551);
            panel1.TabIndex = 2;
            // 
            // tbFingerprint
            // 
            tbFingerprint.DropDownStyle = ComboBoxStyle.DropDownList;
            tbFingerprint.FormattingEnabled = true;
            tbFingerprint.Location = new Point(41, 420);
            tbFingerprint.Name = "tbFingerprint";
            tbFingerprint.Size = new Size(606, 30);
            tbFingerprint.TabIndex = 9;
            tbFingerprint.SelectedIndexChanged += tbFingerprint_SelectedIndexChanged;
            // 
            // tbGender
            // 
            tbGender.DropDownStyle = ComboBoxStyle.DropDownList;
            tbGender.FormattingEnabled = true;
            tbGender.Items.AddRange(new object[] { "Male", "Female" });
            tbGender.Location = new Point(358, 116);
            tbGender.Name = "tbGender";
            tbGender.Size = new Size(289, 30);
            tbGender.TabIndex = 4;
            // 
            // btnUpdate
            // 
            btnUpdate.BackColor = Color.FromArgb(192, 255, 192);
            btnUpdate.Cursor = Cursors.Hand;
            btnUpdate.Location = new Point(41, 488);
            btnUpdate.Name = "btnUpdate";
            btnUpdate.Size = new Size(289, 47);
            btnUpdate.TabIndex = 10;
            btnUpdate.Text = "UPDATE";
            btnUpdate.UseVisualStyleBackColor = false;
            btnUpdate.Click += btnUpdate_Click;
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Font = new Font("Courier New", 11F);
            label7.Location = new Point(41, 396);
            label7.Name = "label7";
            label7.Size = new Size(142, 21);
            label7.TabIndex = 19;
            label7.Text = "Fingerprint:";
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Font = new Font("Courier New", 11F);
            label8.Location = new Point(41, 317);
            label8.Name = "label8";
            label8.Size = new Size(197, 21);
            label8.TabIndex = 17;
            label8.Text = "Registered Doors:";
            // 
            // tbRegisteredDoors
            // 
            tbRegisteredDoors.Location = new Point(41, 344);
            tbRegisteredDoors.Name = "tbRegisteredDoors";
            tbRegisteredDoors.PlaceholderText = "If more than 1, separate by comma. Ex. A14, A15";
            tbRegisteredDoors.Size = new Size(606, 30);
            tbRegisteredDoors.TabIndex = 8;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Font = new Font("Courier New", 11F);
            label5.Location = new Point(358, 235);
            label5.Name = "label5";
            label5.Size = new Size(164, 21);
            label5.TabIndex = 15;
            label5.Text = "Password Hint:";
            // 
            // tbPasswordHint
            // 
            tbPasswordHint.Location = new Point(358, 262);
            tbPasswordHint.Name = "tbPasswordHint";
            tbPasswordHint.PlaceholderText = "Optional";
            tbPasswordHint.Size = new Size(289, 30);
            tbPasswordHint.TabIndex = 7;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Font = new Font("Courier New", 11F);
            label6.Location = new Point(41, 235);
            label6.Name = "label6";
            label6.Size = new Size(153, 21);
            label6.TabIndex = 13;
            label6.Text = "New Password:";
            // 
            // tbPassword
            // 
            tbPassword.Location = new Point(41, 262);
            tbPassword.Name = "tbPassword";
            tbPassword.PlaceholderText = "Enter new password";
            tbPassword.Size = new Size(289, 30);
            tbPassword.TabIndex = 6;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Courier New", 11F);
            label3.Location = new Point(358, 89);
            label3.Name = "label3";
            label3.Size = new Size(87, 21);
            label3.TabIndex = 11;
            label3.Text = "Gender:";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("Courier New", 11F);
            label4.Location = new Point(41, 89);
            label4.Name = "label4";
            label4.Size = new Size(109, 21);
            label4.TabIndex = 9;
            label4.Text = "Username:";
            // 
            // tbUsername
            // 
            tbUsername.Location = new Point(41, 116);
            tbUsername.Name = "tbUsername";
            tbUsername.PlaceholderText = "Enter username";
            tbUsername.Size = new Size(289, 30);
            tbUsername.TabIndex = 3;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Courier New", 11F);
            label2.Location = new Point(358, 15);
            label2.Name = "label2";
            label2.Size = new Size(120, 21);
            label2.TabIndex = 7;
            label2.Text = "Last Name:";
            // 
            // tbLastName
            // 
            tbLastName.Location = new Point(358, 42);
            tbLastName.Name = "tbLastName";
            tbLastName.PlaceholderText = "Enter last name";
            tbLastName.Size = new Size(289, 30);
            tbLastName.TabIndex = 2;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Courier New", 11F);
            label1.Location = new Point(41, 15);
            label1.Name = "label1";
            label1.Size = new Size(131, 21);
            label1.TabIndex = 5;
            label1.Text = "First Name:";
            // 
            // tbFirstName
            // 
            tbFirstName.Location = new Point(41, 42);
            tbFirstName.Name = "tbFirstName";
            tbFirstName.PlaceholderText = "Enter first name";
            tbFirstName.Size = new Size(289, 30);
            tbFirstName.TabIndex = 1;
            // 
            // label10
            // 
            label10.AutoSize = true;
            label10.Font = new Font("Courier New", 11F);
            label10.Location = new Point(41, 162);
            label10.Name = "label10";
            label10.Size = new Size(76, 21);
            label10.TabIndex = 29;
            label10.Text = "Email:";
            // 
            // tbEmail
            // 
            tbEmail.Location = new Point(41, 189);
            tbEmail.Name = "tbEmail";
            tbEmail.PlaceholderText = "Enter email";
            tbEmail.Size = new Size(606, 30);
            tbEmail.TabIndex = 5;
            tbEmail.TabStop = false;
            // 
            // TenantUpdateForm
            // 
            AutoScaleDimensions = new SizeF(12F, 22F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(779, 598);
            Controls.Add(panel1);
            Font = new Font("Courier New", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.FixedToolWindow;
            Margin = new Padding(4, 3, 4, 3);
            Name = "TenantUpdateForm";
            StartPosition = FormStartPosition.CenterParent;
            Text = "UPDATE TENANT";
            Load += TenantUpdateForm_Load;
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Button btnUpdate;
        private Label label7;
        private Label label8;
        private TextBox tbRegisteredDoors;
        private Label label5;
        private TextBox tbPasswordHint;
        private Label label6;
        private TextBox tbPassword;
        private Label label3;
        private Label label4;
        private TextBox tbUsername;
        private Label label2;
        private TextBox tbLastName;
        private Label label1;
        private TextBox tbFirstName;
        private ComboBox tbGender;
        private ComboBox tbFingerprint;
        private Label label10;
        private TextBox tbEmail;
    }
}